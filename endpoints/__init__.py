from endpoints.mails import m_router
from endpoints.phones import p_router
from endpoints.users import u_router


def registration_route(app):
    app.include_router(u_router)
    app.include_router(p_router)
    app.include_router(m_router)
