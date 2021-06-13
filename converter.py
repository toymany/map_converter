import sys
import os

# 変換表
word_map = {
    'B':'"BL"',
    '-':'"--"',
}


# メイン
def main(filename):

    f = open(filename, 'r')

    line = f.readline()
    converted_lines = []

    while line:
        cl = convert_line(line)
        converted_lines.append(cl)
        line = f.readline()

    f.close()
    
    code = to_code(converted_lines, filename)
    save(filename, code)


# コードとして出力
# タブで分離
# 文字列置き換え
def convert_line(line):
    choped_line = line.rstrip('\n')
    words = choped_line.split('\t')
    converted = []
    for w in words:
        c = convert_word(w)
        converted.append(c)

    converted_line = ', '.join(converted)
    code_line = f"        new string[]{{ {converted_line} }},"
    return code_line


# コードにする
def to_code(lines, filename):
    name = os.path.splitext(os.path.basename(filename))[0]
    code_lines = '\n'.join(lines)
    code = f'''public static readonly string[][] {name}= new string[]
    {{
{code_lines}
    }};
    '''
    return code

# 文字列置き換え
def convert_word(src):
    c = word_map.get(src, f'"{src}"')
    return c


# 保存
def save(filename, code):
    name = os.path.splitext(os.path.basename(filename))[0]
    path = f'cs/{name}.cs'
    f = open(path, 'w', encoding='utf-8', newline='\n')
    f.write(code)
    f.close()


# エントリーポイント
if __name__ == "__main__":
    main(sys.argv[1])
