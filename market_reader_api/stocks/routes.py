from flask import Blueprint

stocks_bp = Blueprint('stocks', __name__, url_prefix='/stocks')


@stocks_bp.get('/<stock>')
def index(stock) -> str:
    return f'Stock: {stock}'
