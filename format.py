from datetime import datetime
from fetch import fetch_color_palette


def complementary_color(hex_color):
    hex_color = hex_color.lstrip("#")
    r = 255 - int(hex_color[0:2], 16)
    g = 255 - int(hex_color[2:4], 16)
    b = 255 - int(hex_color[4:6], 16)
    return f"#{r:02x}{g:02x}{b:02x}"


def generate_html_header():
    colors = fetch_color_palette()
    primary_color = colors
    accent_color = complementary_color(primary_color)
    return f"""
    <html>
    <head>
        <style>
            body {{
                color: {accent_color};
                padding: 20px;
                background-color: {primary_color};
            }}
            h2 {{
                color: {accent_color};
                text-align: center;
            }}
            h3 {{
                color: {accent_color};
            }}
            p {{
                color: {accent_color};
                padding: 0 25px;
                text-align: center;
            }}
            .container {{
                background-color: {primary_color};
                padding: 20px;
                border-radius: 10px;
            }}
            .repo {{
                background-color: {primary_color};
                border: 2px solid {accent_color};
                border-radius: 5px;
                padding: 15px;
                margin-bottom: 20px;
            }}
            .repo p {{
                padding: 0px;
                text-align: left;
            }}
            img {{
                max-width: 100%;
                height: auto;
                display: block;
                margin: 0 auto;
                border: 2px solid {accent_color};
                border-radius: 5px;
            }}
            a {{
                color: {accent_color} !important;
            }}
            .footer {{
                margin-top: 20px;
                font-size: 0.9em;
                color: {accent_color};
            }}
        </style>
    </head>
    <body>
    """


def generate_footer():
    return f"""
    <div class="footer">
        <p>Best regards!</p>
    </div>
    """


def format_github_data(repos):

    header = generate_html_header()
    combined_data = f"{header}<div class='container'><h2>GitHub Repositories</h2>"

    for repo in repos:
        name = repo.get("name", "N/A")
        link = repo.get("html_url", "N/A")
        created_at = datetime.strptime(
            repo.get("created_at", "N/A"), "%Y-%m-%dT%H:%M:%SZ"
        ).strftime("%Y-%m-%d")
        language = repo.get("language", "N/A")
        github_profile = repo["owner"].get("html_url", "N/A")

        combined_data += f"""
            <div class="repo">
                <h3>{name}</h3>
                <p><strong>Repository Link:</strong> <a href='{link}'>{link}</a></p>
                <p><strong>Created At:</strong> {created_at}</p>
                <p><strong>Used Language:</strong> {language}</p>
                <p><strong>GitHub Profile:</strong> <a href='{github_profile}'>{github_profile}</a></p>
            </div>
        """

    footer = generate_footer()
    combined_data += f"{footer}</div></body></html>"
    return combined_data


def format_nasa_data(data):
    header = generate_html_header()
    title = data.get("title", "N/A")
    date = data.get("date", "N/A")
    explanation = data.get("explanation", "N/A")
    hdurl = data.get("hdurl", "")
    url = data.get("url", "")

    combined_data = f"{header}<div class='container'><h2>{title}</h2><p><strong>Date:</strong> {date}</p>"
    combined_data += f"<p>{explanation}</p><img src='{url}' alt='{title}'><p><a href='{hdurl}'>View HD Image</a></p>"

    footer = generate_footer()
    combined_data += f"{footer}</div></body></html>"

    return combined_data
