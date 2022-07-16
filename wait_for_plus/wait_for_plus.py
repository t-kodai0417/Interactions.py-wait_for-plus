class select():
    def __init__(self, ctx):
        self.ctx = ctx
    def value(self) -> str:
        return self.ctx.data.values[0]
    def custom_id(self) -> str:
        return self.ctx._json["data"]["custom_id"]
    def options(self) -> list:
        return self.ctx.message.components[0]["components"][0]["options"]
    def author_full(self) ->str:
        return self.ctx._json["member"]["user"]["username"]+"#"+self.ctx._json["member"]["user"]["discriminator"]
    def roles(self) -> list:
        return self.ctx._json["member"]["roles"]
    def channel_id(self) -> int:
        return int(self.ctx._json["channel_id"])
        
