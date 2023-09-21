class Game():
    def __init__(self,
                 id: int,
                 title: str,
                 thumbnail: str,
                 short_description: str,
                 game_url: str,
                 genre: str,
                 platform: str,
                 publisher: str,
                 developer: str,
                 release_date: str,
                 ):
        """
        Instancia um jogo

        Arguments:
            id: Id
            title: Nome
            thumbnail: Imagem de apresentação
            short_description: Descrição curta
            game_url: URL oficial
            genre: Categoria
            platform: Plataforma (Windows, Linux, Android, etc.)
            publisher: Empresa proprietária responsável pela distribuição do jogo
            developer: Empresa que desenvolveu o jogo
            release_date: Data de lançamento
        """
        self.id = id or ''
        self.title = title or ''
        self.thumbnail = thumbnail or ''
        self.short_description = short_description or ''
        self.game_url = game_url or ''
        self.genre = genre or ''
        self.platform = platform or ''
        self.publisher = publisher or ''
        self.developer = developer or ''
        self.release_date = release_date or ''
