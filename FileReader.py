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
            with open(self.path, 'r', errors='ignore') as f_in:                     # open path and ignore errors
                self.text = list(filter(None, (line.rstrip() for line in f_in)))    # remove all blank lines by filter 
        except IOError:
            print('cannot open', self.path) # if IOError/ not exist
    
    def isRequired(self, factor):   # check if it is an required file
        if factor:                  # check factor is true or not empty
            self.req_file = True
        return self.req_file    
    
    def requiredHostname(self):                             # find hostname
        substring = '(#show clock|#enable)' 
        for line in self.text:
            if re.search(substring, line):                  # if found substring in line, then this line include hostname
                self.hostname = re.sub(substring, '', line) # get only hostname without substring
                break                                       # break loop
        return self.hostname
        

    def requiredModel(self):                                # find model
        substring = '.*(M|m)odel (N|n)umber.*:'
        for line in self.text:
            if re.search(substring, line):                  # if found substring in line, then this line include model
                self.model = re.sub(substring, '', line)    # get only model number
                break                                       # break loop
        return self.model

    def requiredSerial(self):                               # find Serial number
        substring = '(System (S|s)erial (N|n)umber|Chassis (S|s)erial (N|n)umber).*:'
        for line in self.text:
            if re.search(substring, line):                  # if found substring in line, then this line include Serial Number
                self.serial = re.sub(substring, '', line)   # get only serial number
                break                                       # break loop
        return self.serial
    
    def requiredVersion(self):                              # find software version
        substring = '(Cisco)* IOS.*Software.*Version'
        for line in self.text:
            if re.search(substring, line):                   # if found substring in line, then this line include software version
                self.version = re.sub(substring, '', line)   # get only serial number
                self.version = re.sub('(,*\sRELEASE|\s-\sExtended).*' ,'', self.version)
                break                                        # break loop
        return self.version
   
    def requiredInterfaceDescription(self):                     # find interface description section
        command_substring = '.*#show interface description'
        interfaces_substring = '(Interface|Port|(Fa)|(Gi)|(Po)|(Te)|(Vl)).*'
        interface_description = []
        modify_interface_description = []
        read_section = False                                    # init read_section
        
        for line in self.text:
            if re.search(command_substring, line):              # if command exist in line, then next line is required section
                read_section = True                             # so read_section is true/ can start to read next line
                continue                                        # so continue
            elif read_section:                                  # check if read_section is true
                if re.search(command_substring, line):          # if command exist in line again, then we want to read next line
                    continue                                    # so continue
                elif not (self.hostname in line):               # if hostname not exist in line/ the command result display is unfinished
                    if re.search(interfaces_substring, line):   # to avoid warning message, then check if a line start with Interface/Port
                        interface_description.append(line)      # add matching line into list
                else:                                           # if the command result display is finished
                    read_section = False                        # so read_section is false
                    break                                       # break loop
        
        for element in interface_description:
            if element == interface_description[0]:             # if first row, then split first row to column name
                items = element.split()
            else: 
                items = re.split(r'\s{4}', element)             # split a string by 4 whitespaces
                items = list(filter(None, items))               # remove empty string by filter
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
            items = re.split(r'\s{1,}',items)                         # split a string at least 1 whitespace
            # temp = re.findall('.*?()', temp)
            # items = list(filter(None, items))

            if len(items) == 6:                                       # if column number = 6, then combine/join column
                items[4:6] = [''.join(items[4:6])]
            
            modify_interface_status.append(items)
        
        return modify_interface_status
    