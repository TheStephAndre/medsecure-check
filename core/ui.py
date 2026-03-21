from fastapi.templating import Jinja2Templates

import core.wording as wording

templates = Jinja2Templates(directory="templates")

# Move your global injections here
templates.env.globals.update(
    {
        "PRODUCT": wording.PRODUCT,
        "DISCLAIMERS": wording.DISCLAIMERS,
        "RESULT": {**wording.RESULT, "risk_levels": wording.RISK_LEVELS},
    }
)
