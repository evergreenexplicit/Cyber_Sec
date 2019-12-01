import DecryptorStats as d
def main():
    dec = d.Decryptor('input1.txt')
    dec.get_data_from_file()
    dec.output()


if __name__ == '__main__':
    main()
