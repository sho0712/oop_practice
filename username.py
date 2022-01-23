"""
データ型の宣言：　username
　属性：実際のユーザー名
　ルール：ユーザー名は４文字以上２０文字以内
　できること：ユーザー名を大文字に変換する
"""


class UserName:
    def __init__(self, name):
        # 　nameのチェック
        if not (4 <= len(name) and len(name) <= 20):
            raise ValueError(f'{name}ルール違反です')
        self.name = name

    def battle_name(self):
        return self.name.upper()


bob = UserName(name='Bob Swith')
# tom = UserName(name='Tom Ford')

print(bob.name)
print(bob.battle_name())
# print(tom.name)
