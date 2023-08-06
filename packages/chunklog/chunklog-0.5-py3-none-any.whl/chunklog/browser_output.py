from chunklog.colored_output import parse_html_diff
import html


def parse_html_output(entries, highlight_diff, handle):
    heading = (
        f"History for chunk {entries[0].id}"
        if entries[0]
        else f"The chunk had no history"
    )
    date_headers = "<th></th>\n"
    files = ""
    commits = ""
    authors = ""
    messages = ""
    texts = ""

    # all attributes except text made to string of table elements
    for entry in entries:
        date_headers = date_headers + f"<th>{entry.date[:-9]}</th>\n"
        files = files + f"<td>{entry.file}</td>\n"
        commits = commits + f"<td>{entry.commit}</td>\n"
        authors = authors + f"<td>{entry.author}</td>\n"
        messages = messages + f"<td>{entry.message}</td>\n"

    # text; also check if diff coloring
    previous_entry = ""
    if highlight_diff:
        for entry in entries:
            if previous_entry == "":
                texts = (
                    texts
                    + f'<td style="white-space: pre-wrap">{(parse_html_diff("", html.escape(entry.text)))}</td>\n'
                )
            else:
                texts = (
                    texts
                    + f'<td style="white-space: pre-wrap">{parse_html_diff(html.escape(previous_entry.text), html.escape(entry.text))}</td>\n'
                )
            previous_entry = entry
    else:
        for entry in entries:  # pragma: no cover
            texts = (
                texts
                + f'<td style="white-space: pre-wrap">{html.escape(entry.text)}</td>\n'
            )

    # write to html file
    with open(handle, "w") as file:
        file.write(
            f"""
                    <html>
                    <head>
                    <style>
                    *{{
                        box-sizing: border-box;
                        -webkit-box-sizing: border-box;
                        -moz-box-sizing: border-box;
                    }}
                    body{{
                        font-family: Helvetica;
                        -webkit-font-smoothing: antialiased;
                        background: rgba( 71, 147, 227, 1);
                    }}
                    h2{{
                        text-align: center;
                        font-size: 18px;
                        text-transform: uppercase;
                        letter-spacing: 1px;
                        color: white;
                        padding: 30px 0;
                    }}

                    /* Table Styles */

                    .table-wrapper{{
                        margin: 10px 70px 70px;
                        box-shadow: 0px 35px 50px rgba( 0, 0, 0, 0.2 );
                    }}

                    .fl-table {{
                        border-radius: 5px;
                        font-size: 12px;
                        font-weight: normal;
                        border: none;
                        border-collapse: collapse;
                        width: 100%;
                        max-width: 100%;
                        background-color: white;
                    }}

                    .fl-table td, .fl-table th {{
                        text-align: left;
                        vertical-align: top;
                        padding: 8px;
                    }}

                    .fl-table td {{
                        border-right: 1px solid #f8f8f8;
                        font-size: 12px;
                    }}

                    .fl-table thead th {{
                        color: #ffffff;
                        background: #4FC3A1;
                    }}


                    .fl-table thead th:nth-child(odd) {{
                        color: #ffffff;
                        background: #324960;
                    }}

                    .fl-table tr:nth-child(even) {{
                        background: #F8F8F8;
                    }}

                    /* Responsive */

                    @media (max-width: 767px) {{
                        .fl-table {{
                            display: block;
                            width: 100%;
                        }}
                        .table-wrapper:before{{
                            content: "Scroll horizontally >";
                            display: block;
                            text-align: right;
                            font-size: 11px;
                            color: white;
                            padding: 0 0 10px;
                        }}
                        .fl-table thead, .fl-table tbody, .fl-table thead th {{
                            display: block;
                        }}
                        .fl-table thead th:last-child{{
                            border-bottom: none;
                        }}
                        .fl-table thead {{
                            float: left;
                        }}
                        .fl-table tbody {{
                            width: auto;
                            position: relative;
                            overflow-x: auto;
                        }}
                        .fl-table td, .fl-table th {{
                            padding: 20px .625em .625em .625em;
                            height: 60px;
                            vertical-align: middle;
                            box-sizing: border-box;
                            overflow-x: hidden;
                            overflow-y: auto;
                            width: 120px;
                            font-size: 13px;
                            text-overflow: ellipsis;
                        }}
                        .fl-table thead th {{
                            text-align: left;
                            border-bottom: 1px solid #f7f7f9;
                        }}
                        .fl-table tbody tr {{
                            display: table-cell;
                        }}
                        .fl-table tbody tr:nth-child(odd) {{
                            background: none;
                        }}
                        .fl-table tr:nth-child(even) {{
                            background: transparent;
                        }}
                        .fl-table tr td:nth-child(odd) {{
                            background: #F8F8F8;
                            border-right: 1px solid #E6E4E4;
                        }}
                        .fl-table tr td:nth-child(even) {{
                            border-right: 1px solid #E6E4E4;
                        }}
                        .fl-table tbody td {{
                            display: block;
                            text-align: center;
                        }}
                    }}
                    </style>
                    </head>

                    <body>
                    <h2>{heading}</h2>
                    <div class="table-wrapper">
                        <table class="fl-table">
                            <thead>
                            <tr>
                                {date_headers}
                            </tr>
                            </thead>
                            <tbody>
                            <tr>
                                <td>File</td>
                                {files}
                            </tr>
                            <tr>
                                <td>Commit</td>
                                {commits}
                            </tr>
                            <tr>
                                <td>Author</td>
                                {authors}
                            </tr>
                            <tr>
                                <td>Message</td>
                                {messages}
                            </tr>
                            <tr>
                                <td>Text</td>
                                {texts}
                            </tr>
                            <tbody>
                        </table>
                    </div>
                    </body>
                    </html>
                    """
        )
