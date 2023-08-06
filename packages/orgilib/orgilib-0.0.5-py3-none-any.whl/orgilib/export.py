import json

def wprint_dataframe():
    print('orangelib.line: df 파라미터 에러.')
def wprint_dataframe_x():
    print('orangelib.line: x 컬럼이 DataFrame 에 없습니다.')
def wprint_x():
    print('orangelib.line: x 파라미터가 없습니다.')
def wprint_dataframe_y():
    print('orangelib.line: y 컬럼이 DataFrame 에 없습니다.')
def wprint_y():
    print('orangelib.line: y 파라미터가 없습니다.')
def wprint_unkown_type():
    print('알수 없는 차트타입')

def export(**kwargs):
    df = kwargs.get('df', None)
    if df is None:
        wprint_dataframe()
    else:
        try:
            response = {
                'exportType': 'data',
                'rows': df.to_json(orient='records'),
            }
            print(json.dumps(response))
        except:
            print('orangelib 에러: export function ')