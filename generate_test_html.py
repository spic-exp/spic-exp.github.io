s = ['<!DOCTYPE html>','<htmlmargin:0; padding:0; overflow:hidden>','<body>','<svg position="fixed" top="0" left="0" height="3200" width="3200" viewbox="0 0 8192 8192">']

#<rect x="0" y="0" width="100" height="8192" stroke="black" stroke-width="20" fill="black" transform = "rotate(4 0 0)" />
for i in range(30):
    new_str = '<rect x="0" y="0" width="100" height="8192" stroke="black" stroke-width="20" fill="black" transform = "rotate({0} 0 0)" />'.format(8)
    s.append(new_str)

s.append('</svg>')
s.append('</body>')
s.append('</html>')    

with open('index.html', 'w') as f:
    for line in s:
        f.write(line)
        f.write('\n')