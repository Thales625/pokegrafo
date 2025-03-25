class Pokemon:
    def __init__(self, name, stats, id):
        self.name = name
        self.stats = stats 
        self.initial_stats = stats.copy()
        self.id = id
        self.acessos = 0
    
    def __str__(self):
        card_border = "+" + "-" * 30 + "+"
        card_title = f"| {self.name.capitalize():^28} |"
        acessos_line = f"| {(f'{self.acessos} Acesso(s)'):^28} |"
        stats_lines = "\n".join([f"| {stat_name.replace('-', ' ').title():<16}: {value:<10} |" for stat_name, value in self.stats.items()])
        return f"""{card_border}
{card_title}
{acessos_line}
{card_border}
{stats_lines}
{card_border}
""".strip()

    def __repr__(self):
        return f"<Object {self.name}>"