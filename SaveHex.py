import numpy as np

class SaveHex:
    def __init__(self, hex_dump, file_name):
        self.hex = hex_dump
        self.file = file_name
        self.text_file = open(self.file, 'a+')

    def write_data(self, text):
        self.text_file.write(text + '\n')

    def close(self):
        self.text_file.close()

    @staticmethod
    def hex2string(hex_input):
        if hex_input < 16:
            out_put = '0' + hex(hex_input)[-1]
        else:
            out_put = hex(hex_input)[-2] + hex(hex_input)[-1]
        return out_put

    def save_data(self):
        cntr_fill = 16 - (len(self.hex) % 16)
        cntr_zr = np.zeros(cntr_fill, dtype=int)
        self.hex = np.concatenate((self.hex, cntr_zr))
        print(len(self.hex))
        for i in range(0, len(self.hex), 16):

            print(i)
            string = ('%x  %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s    ................' \
                  % (i,self.hex2string(self.hex[i]), self.hex2string(self.hex[i+1]), self.hex2string(self.hex[i+2]), self.hex2string(self.hex[i+3]), self.hex2string(self.hex[i+4]), self.hex2string(self.hex[i+5]), \
                     self.hex2string(self.hex[i+6]), self.hex2string(self.hex[i+7]), self.hex2string(self.hex[i+8]), self.hex2string(self.hex[i+9]), self.hex2string(self.hex[i+10]), self.hex2string(self.hex[i+11]), \
                     self.hex2string(self.hex[i+12]), self.hex2string(self.hex[i+13]), self.hex2string(self.hex[i+14]),  self.hex2string(self.hex[i+15])))
            self.write_data(string)
            #SaveHex.hex2string()
            print(string)
        self.close()

if __name__ == "__main__":
    pass
