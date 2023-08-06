import json
import re


class FileTypeFinder:

    def __find_file_type_using_content_disposition(self, response) -> str:

        pattern = re.compile("filename=(.*)$")
        filename = pattern.search(response.headers['Content-Disposition']).group(1)
        file_type = filename.split('.')[-1]
        if file_type:
            return file_type, True
        else:
            return None, False

    def __find_file_type_using_content_type(self, response_content_type) -> str:

        with open(r'src/content_type.json', 'r') as file:
            file_data = file.read()
            content_type_dict = json.loads(file_data)

        file_types_list = list(content_type_dict['file_content_type'].keys())
        content_type_list = list(content_type_dict['file_content_type'].values())

        for index, content_types in enumerate(content_type_list):
            for content_type in content_types:
                if content_type in response_content_type:
                    file_type = file_types_list[index]
                    if file_type:
                        return file_type, True
        return None, False

    def __find_file_type_using_file_signature(self,response_content) -> str:
        with open(r'src/file_signatures.json', 'r') as file:
            file_data = file.read()
            file_signature_dict = json.loads(file_data)

        file_types_list = list(file_signature_dict.keys())
        file_signature_list = list(file_signature_dict.values())

        response_hex = response_content[0:20].hex()
        
        for index, file_signatures in enumerate(file_signature_list):
            for file_signature in file_signatures:
                if response_hex.startswith(file_signature):
                    file_type = file_types_list[index]
                    if file_type:
                        return file_type, True
        return None, False

    def __find_file_type_using_response_path(self, response) -> str:
        pass
        #return file_type, True if file_type else None, False

    def find_file_type(self, response) -> str:
        file_type_found = False
        if 'Content-Disposition' in response.headers:
            file_type, file_type_found = self.__find_file_type_using_content_disposition(response)

        if not file_type_found and 'Content-Type' in response.headers:
            file_type, file_type_found = self.__find_file_type_using_content_type(response.headers['Content-Type'])
            if file_type_found: return file_type
            
        if not file_type_found:
            file_type, file_type_found = self.__find_file_type_using_file_signature(response.content)
            if file_type_found: return file_type

        if not file_type_found:
            file_type, file_type_found = self.__find_file_type_using_response_path(response)
            if file_type_found: return file_type



        
        




    