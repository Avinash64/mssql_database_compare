'''<table class="table table-dark">
        <thead>
          <tr>
            <th scope="col">#</th>
            <th scope="col">First</th>
            <th scope="col">Last</th>
            <th scope="col">Handle</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
          </tr>
          <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
          </tr>
          <tr>
            <th scope="row">3</th>
            <td>Larry</td>
            <td>the Bird</td>
            <td>@twitter</td>
          </tr>
        </tbody>
      </table>'''


def table(nested_list):
    newline = '\n'
    html = '<table class="table table-dark">'
    for index, row in enumerate(nested_list):
        html += f'<tr>\n<th scope="row">{row[0]}</th>\n{newline.join([f"<td>{i}</td>" for i in row[1:]])}\n</tr>'
    html += '</tbody>\n</table>'
    return html

t = table([(1, 'Tilted Towers'), (2, 'Pleasant Park'), (3, 'Retail Row'), (4, 'Greasy Grove'), (5, 'Loot Lake'), (6, 'Salty Springs'), (7, 'Shifty Shafts'), (8, 'Wailing Woods'), (9, 'Dusty Divot'), (10, 'Lucky Landing'), (11, 'Risky Reels'), (12, 'Lonely Lodge'), (13, 'Snobby Shores'), (14, 'Fatal Fields'), (15, 'Flush Factory'), (16, 'Haunted Hills'), (17, 'Junk Junction'), (18, 'Tomato Temple'), (19, 'Lazy Links'), (20, 'Paradise Palms'), (21, 'Dirty Docks'), (22, 'Frosty Flights'), (23, 'Holly hedges'), (24, 'Craggy Cliffs')])
user_data = [
    [0, "Alice", 25, "alice@example.com", "New York", "Engineer", 65000],
    [1, "Bob", 30, "bob@example.com", "Los Angeles", "Designer", 72000],
    [2, "Charlie", 22, "charlie@example.com", "Chicago", "Developer", 60000],
    [3, "David", 28, "david@example.com", "Houston", "Analyst", 68000],
    [4, "Eve", 35, "eve@example.com", "San Francisco", "Manager", 85000],
    [5, "Frank", 40, "frank@example.com", "Seattle", "Director", 95000],
    [6, "Grace", 27, "grace@example.com", "Boston", "Consultant", 70000],
    [7, "Hank", 32, "hank@example.com", "Denver", "Architect", 78000],
    [8, "Ivy", 29, "ivy@example.com", "Miami", "Scientist", 73000],
    [9, "Jack", 24, "jack@example.com", "Atlanta", "Technician", 62000]
]

t = table(user_data)

def gen_html(template_file, table_html):
    with open(template_file, encoding='utf-8') as f:
        template = f.read()
    return template.replace('{{table}}',table_html)
# template = gen_html('index.html', t)
