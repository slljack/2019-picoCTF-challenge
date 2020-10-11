import requests

r = requests.get("https://2019shell1.picoctf.com/problem/49886/")

html_code = r.text

split = int(html_code[html_code.find("split")+8])
ret_flag = ''

key1 = html_code.find("substring(")
range_str = html_code[key1+10 : html_code.find(')', key1)]
frag = html_code[key1+10 : html_code.find(')', key1)]
start = int(range_str[0])
end = split #end = range_str[9]
ret_flag += html_code[html_code.find('\'', key1)+1:html_code.find('\'', html_code.find('\'', key1)+1)]
key2 = html_code.find("substring(", key1+1)

start_list = []
str_list = []
while(key2 != -1):
    range_str = html_code[key2 + 16: html_code.find(')', key2)]
    if(not range_str[0].isdigit()):
        start = split
    else:
        start = int(range_str[0])*split
    end = int(html_code[html_code.find('*', key2+20)+1:html_code.find('*', key2+20)+2])*split
    start_list.append(start)
    str_list.append(html_code[html_code.find('\'', key2)+1:html_code.find('\'', html_code.find('\'', key2)+1)])
    z = [x for _,x in sorted(zip(start_list, str_list))]
    key2 = html_code.find("substring(", key2 + 1)

ret_flag += "".join(z)
print(ret_flag)
