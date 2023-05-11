from blacksheep import redirect
from blacksheep.server.controllers import get, Controller


class DefaultRedirect(Controller):

    @get("/")
    async def default_redirect(self) -> redirect:
        return redirect('/docs')
