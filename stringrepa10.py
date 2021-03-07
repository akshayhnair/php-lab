m_string = input("type a string ")
char=m_string[0]
m_string = m_string.replace(char,'$')
print(char+m_string[1:])