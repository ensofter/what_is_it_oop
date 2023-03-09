text = 'hello'
parts = ['<p>', text, '</p>']

words = ['hello', 'world']

if __name__ == '__main__':
    print(''.join(parts))

    parts = ['<ul>']
    for word in words:
        parts.append(f' <li>{word}</li>')
    parts.append('</ul>')
    print('\n'.join(parts))

