import re


class Preprocess_xml:

    def search_space_ampersand(self, string):
        amp = re.sub(r'\s*[&]\s*|(<=\w*)[&](?=\w*)', ' &amp; ', string)
        if amp:
            return amp #string.replace(amp.group(0), ' &amp; ')

        return string

    def search_dash(self, string):
        dash = re.sub(r'-<', '<', string)
        if dash:
            return dash #string.replace(dash.group(0), '<')

        return string


    def search_nested_quote(self, string):
        route = re.search(r'(?<=[,])ROUTE 1(?=[\s\",])', string)
        if not route:

            frac_regex = r'(?<=\/\d)\"(?=[\s\",])'
            dec_regex = r'(?<=\.\d\d)\"(?=[\s\",])|(?<=\.\d)\"(?=[\s\",])'
            inch_regex = r'(?<=\s\d\d)\"(?=[\s\",])'
            name_sub_string_regex = r'(?<=name=)(\".*?\")(?=\sitem_id)'

            sub = re.search(name_sub_string_regex, string)
            quot = ''
            if sub:
                fixed_content = re.sub(f'{frac_regex}|{dec_regex}|{inch_regex}', '&quot;', sub.group(0))

                quot = re.sub(name_sub_string_regex, fixed_content, string)

            if quot:
                return quot
            
        return string 


    def return_processed_xml(self, xml_txt_path):
        clean_xml_string = ''
        with open(xml_txt_path, 'r') as unprocessed_xml:
            for line in unprocessed_xml.readlines():
                line = self.search_dash(line)
                line = self.search_space_ampersand(line)
                line = self.search_nested_quote(line)
                clean_xml_string += line

        return clean_xml_string
            
