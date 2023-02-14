from passlib.context import CryptContext

CRIPTO = CryptContext(schemes=['md5_crypt'], deprecated='auto')


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """
    Função para verificar se a senha está correta, comparando a senha em texto puro, 
    informada pelo usuário,e o Hash da senha que estará salvo no banco de dados durante 
    a criação da conta.
    """
    return CRIPTO.verify(senha, hash_senha)


def gerar_hash_senha(senha: str) -> str:
    """
    Função que retorna o hash da senha.
    """
    return CRIPTO.hash(senha)