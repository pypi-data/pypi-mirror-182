def validate_adhar_details(adhar_number,adhar_name):
    if len(adhar_number)!= 12:
        print('Invalid Adhar Number, Pleas re-enter: ')
        return False
    if len(adhar_name)<3:
        print('Invalid Adhar Name, Please re-enter:')
        return False
    return True
