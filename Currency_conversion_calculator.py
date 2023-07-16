from currency_classes import USD, ILS

user_choice = None
previous_user_choices = []


# The func let the user choose the conversion flow
def get_value():
    global user_choice

    try:
        user_choice = int(input('please choose: [1] USD-->ILS OR [2] ILS-->USD: '))
    except ValueError:
        print('Invalid character')

    previous_user_choices.append(user_choice)

    if user_choice == 1:
        value_to_convert = float(input('please enter an amount to convert: '))
        usd = USD(value_to_convert)
        print(usd.conversion_value)

    elif user_choice == 2:
        value_to_convert = float(input('please enter an amount to convert: '))
        ils = ILS(value_to_convert)
        print(ils.conversion_value)
    else:
        print('Please try again with options 1 or 2')


# The func concatenate the usd/ils lists to be able to print the conversion flow of each item in the list as string
def merge_result_archive_usd():
    joined_list = ' '.join(USD.resultArchive)
    return joined_list


def merge_result_archive_ils():
    joined_list = ' '.join(ILS.resultArchive)
    return joined_list


# The func checks the previous selections of the user in order to print the conversion flow of usd ans ils
def check_values_in_array(array):

    if 1 in array and 2 in array:
        print(merge_result_archive_ils())
        print(merge_result_archive_usd())

    elif 1 in array:
        print(merge_result_archive_usd())

    elif 2 in array:
        print(merge_result_archive_ils())


# This function calls other functions in order to give the user an option to restart the calculator
def main():

    print('Welcome to currency converter...')

    x = "Y"
    while x.upper() == 'Y':
        get_value()
        x = input('Do you want to start over Y / N.')

    print('Thanks for using our currency converter.')
    check_values_in_array(previous_user_choices)
    file = open('Currency_conversion_calculator_results.txt', 'w')
    file.write(f"{merge_result_archive_ils()}\n{merge_result_archive_usd()}")


main()
d