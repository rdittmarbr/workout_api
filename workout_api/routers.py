from fastapi import APIRouter
from workout_api.atleta.controller import router as atleta_router
from workout_api.categorias.controller import router as categorias_router
from workout_api.centro_treinamento.controller import router as centro_treinamento_router

# Cria uma instância do APIRouter para agrupar todas as rotas da API
api_router = APIRouter()

# Inclui o router de atleta com um prefixo e uma tag
api_router.include_router(atleta_router, prefix='/atletas', tags=['atletas'])

# Inclui o router de categorias com um prefixo e uma tag
api_router.include_router(categorias_router, prefix='/categorias', tags=['categorias'])

# Inclui o router de centro de treinamento com um prefixo e uma tag
api_router.include_router(centro_treinamento_router, prefix='/centros_treinamento', tags=['centros_treinamento'])
