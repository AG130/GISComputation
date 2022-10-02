import json
dict1={'value':
                    [
                        {'name': '路人乙', 'sex': '女',
                    'id_card': '17098098', 'checkdata': '206251989',
                    'result': '阳性', 'responsibilityman': '负责人2',
                    'lon': '114.408', 'lat': '30.53'},
                        ]
                    }
print(dict1.get('value')[0])