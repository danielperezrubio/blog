import bleach


async def clean_html(content: str):
    allowed_tags = [
        "h1",
        "h2",
        "h3",
        "strong",
        "em",
        "u",
        "s",
        "sub",
        "sup",
        "blockquote",
        "pre",
        "ol",
        "ul",
        "li",
        "p",
        "a",
        "br",
        "img",
        "span",
    ]
    allowed_attributes = {
        "a": ["href", "target"],
        "img": ["src"],
        "p": ["class"],
        "pre": ["class"],
        "span": ["class"],
    }
    cleaned_post = bleach.clean(
        content, tags=allowed_tags, attributes=allowed_attributes
    )
    return cleaned_post
