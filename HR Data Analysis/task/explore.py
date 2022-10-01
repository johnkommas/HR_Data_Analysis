import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    # write your code here

    # XML to DF
    df_A_office_data = pd.read_xml('../Data/A_office_data.xml')
    df_B_office_data = pd.read_xml('../Data/B_office_data.xml')
    df_hr_data = pd.read_xml('../Data/hr_data.xml')

    index_a = df_A_office_data.employee_office_id.values
    index_a = ["A"+ str(i) for i in index_a]

    index_b = df_B_office_data.employee_office_id.values
    index_b = ["B"+ str(i) for i in index_b]

    df_A_office_data['index'] = index_a
    df_A_office_data.set_index('index', drop=True, inplace=True)

    df_B_office_data['index'] = index_b
    df_B_office_data.set_index('index', drop=True, inplace=True)

    df_hr_data.set_index("employee_id", drop=True, inplace=True)

    print(df_A_office_data.index.to_list())
    print(df_B_office_data.index.to_list())
    print(df_hr_data.index.to_list())



