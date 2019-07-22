import re

class FileReader:

    def __init__(self, path):
        self.path = path
        self.text = []
        self.req_file = False
        self.hostname = ''
        self.model = ''
        self.serial = ''
        self.version = ''

    def readFile(self):
        try: 
            with open(self.path, 'r', errors='ignore') as f_in:
                self.text = list(filter(None, (line.rstrip() for line in f_in)))
        except IOError:
            print('cannot open', self.path)
    
    def isRequired(self, factor):
        if factor:
            self.req_file = True
        return self.req_file
    
    def requiredHostname(self):
        substring = '(#show clock|#enable)' 
        for line in self.text:
            if re.search(substring, line):
                self.hostname = re.sub(substring, '', line)
                break
        return self.hostname

    def requiredModel(self):
        substring = '.*(M|m)odel (N|n)umber.*:'
        for line in self.text:
            if re.search(substring, line):
                self.model = re.sub(substring, '', line)
                break
        return self.model

    def requiredSerial(self):
        substring = '(System (S|s)erial (N|n)umber|Chassis (S|s)erial (N|n)umber).*:'
        for line in self.text:
            if re.search(substring, line):
                self.serial = re.sub(substring, '', line)
                break
        return self.serial
    
    def requiredVersion(self):
        substring = '(Cisco)* IOS.*Software.*Version'
        for line in self.text:
            if re.search(substring, line):
                self.version = re.sub(substring, '', line)
                self.version = re.sub(',| RE\w+', '', self.version)
                break
        return self.version

    def requiredInterfaceDescription(self):
        command_substring = '.*#show interface description'
        interfaces_substring = '(Interface|Port|(Fa)|(Gi)|(Po)|(Te)|(Vl)).*'
        interface_description = []
        modify_interface_description = []
        read_section = False
        
        for line in self.text:
            if re.search(command_substring, line):
                read_section = True
                continue
            elif read_section:
                if not (self.hostname in line):
                    if re.search(interfaces_substring, line): 
                        interface_description.append(line)
                else:
                    read_section = False
                    break
        
        for element in interface_description:
            if element == interface_description[0]: # if label name, then split label name to column name
                items = element.split()
            else: 
                items = re.split(r'\s{4}', element) # split a string by 4 whitespaces
                items = list(filter(None, items)) # remove empty string by filter
            modify_interface_description.append(items)

        return modify_interface_description
    
    def requiredInterfaceStatus(self):
        command_substring = '.*#show interface status$'
        interfaces_substring = '(Interface|Port|(Fa)|(Gi)|(Po)|(Te)|(Vl)).*'
        remove_substring = '\s{1,}.*(connected|notconnect|disabled|inactive|monitoring)|Name|Status'
        replace_string = ''
        interface_status = []
        modify_interface_status = []
        read_section = False

        for line in self.text:
            if re.search(command_substring, line):
                read_section = True
                continue
            elif read_section:
                if re.search(command_substring, line):
                    continue
                elif not (self.hostname in line):
                    if re.search(interfaces_substring, line): 
                        interface_status.append(line)
                else:
                    read_section = False
                    break
        
        for element in interface_status:
            items = re.sub(remove_substring, replace_string, element) # remove substring and replace with empty string
            items = re.split(r'\s{1,}',items) # split a string at least 1 whitespace
            # temp = re.findall('.*?()', temp)
            # items = list(filter(None, items))

            if len(items) == 6:    # if column number = 6, then combine/join column
                items[4:6] = [''.join(items[4:6])]
            
            modify_interface_status.append(items)
        
        return modify_interface_status
    