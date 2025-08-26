import codecs
import re
import html


def delete_html_tags(html_file, result_file='cleaned.txt', drop_empty=True):


    # 1) Зчитуємо вихідний файл
    with codecs.open(html_file, 'r', 'utf-8') as file:
        text = file.read()

    # 2) Видаляємо теги: все від '<' до '>'
    no_tags = re.sub(r"<.*?>", "", text, flags=re.DOTALL)

    # 3) Декодуємо HTML-сутності
    no_tags = html.unescape(no_tags)

    # 4) Розбиваємо на рядки, прибираємо зайві пробіли по краях
    lines = [line.strip() for line in no_tags.splitlines()]

    # 5) Прибираємо порожні рядки або рядки без інформації
    if drop_empty:
        # залишаємо рядки, де є хоч щось, крім пробілів
        lines = [ln for ln in lines if ln]

    # 6) Записуємо результат
    with codecs.open(result_file, 'w', 'utf-8') as out:
        out.write("\n".join(lines))
