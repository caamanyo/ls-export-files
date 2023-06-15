"""Manage Limesurvey petitions."""

from limesurveyrc2api.limesurvey import LimeSurvey
from limesurveyrc2api.exceptions import LimeSurveyError
from collections import OrderedDict
import os
import shutil
import constants as c
from exceptions import ParticipantError


class LSCon(LimeSurvey):
    def __init__(self, url, username):
        """Initialize class."""
        super().__init__(url, username)

    def get_participant_by_token(self, surveyid, token):
        """Fetch participant data from a survey."""
        try:
            return self.token.get_participant_properties(
                surveyid, token_query_properties={"token": token})
        except LimeSurveyError as e:
            raise ParticipantError("Aquest token no existeix.")

    def extract_all_participant_files(self):
        """Get all files imported by a participant based on her token."""

        def ensure_dictionary(suspect):
            check = isinstance(suspect, dict)
            if not check:
                return {}
            return suspect

        def remove_all_files(path):
            """Remove all files from a selected folder."""
            for filename in os.listdir(path):
                file_path = os.path.join(path, filename)
                try:
                    if os.path.isfile(file_path) or os.path.islink(file_path):
                        os.unlink(file_path)
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                except Exception as e:
                    print('Failed to delete %s. Reason: %s' % (file_path, e))

        # Path where files will be exported.
        exported_path = "fitxers exportats"

        # Participant token to search for.
        token = input("Token de l'alumne: ")
        al_data = self.get_participant_by_token(c.GENERAL_FORM_ID, token)
        breakpoint()

        al_fullname = f"{al_data['lastname']}, {al_data['firstname']}"
        al_cicle = al_data["attribute_3"]
        if len(al_cicle) > 3:
            al_cicle = al_cicle[3]

        # Create alumnus folder
        al_path = f"{exported_path}/{al_cicle}/{al_fullname}"
        if not os.path.exists(al_path):
            os.makedirs(al_path)
        else:
            remove_all_files(al_path)

        params = OrderedDict([
            ("sessionkey", self.session_key),
            ("surveyid", al_data["attribute_4"]),
            ("token", token)
        ])

        # Get a list of all the files related to that participant
        cicle_response = self.query("get_uploaded_files", params)
        cicle_files = ensure_dictionary(cicle_response)

        # TODO: Extract files form the general form.
        params["surveyid"] = c.GENERAL_FORM_ID
        general_response = self.query("get_uploaded_files", params)
        general_files = ensure_dictionary(general_response)

        results = {**cicle_files, **general_files}

        for [key, value] in results.items():
            # Check if table exists
            if key == "status":
                print("La taula de participants no existeix.")
                continue

            # Decode file
            with open(f"{al_path}/{al_fullname} - {value['meta']['question']['title']}.pdf", "wb") as f:
                f.write(base64.b64decode(value["content"]))

        # Close the session.
        self.close()