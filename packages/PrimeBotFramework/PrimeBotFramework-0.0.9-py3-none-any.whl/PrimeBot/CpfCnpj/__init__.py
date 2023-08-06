import requests
from PrimeBot.CpfCnpj.model import Endereco, DadosEmpresa, Erro
from PrimeBot.CpfCnpj.api_codes import Package, Error

def set_token(token: str) -> None:
    global TOKEN
    TOKEN = token


def consulta_cnpj(cnpj: str) -> dict:
    base_url = "https://api.cpfcnpj.com.br/"
    if not TOKEN:
        raise Exception("Token não definido")
    CALL_URL = f"{base_url}/{TOKEN}/{Package.CNPJ_C.value}/{cnpj}"
    response = requests.get(CALL_URL)
    response_json = response.json()
    error_list = [
        Error.CNPJ_INCOMPLETO.value,
        Error.CNPJ_INVALIDO.value,
        Error.CNPJ_INEXISTENTE.value,
        Error.TOKEN_INVALIDO.value,
        Error.FORNECEDOR_INDISPONIVEL.value,
        Error.IMPOSSIVEL_CONSULTAR.value,
        Error.CONTA_BLOQUEADA.value,
        Error.CREDITOS_INSUFICIENTES.value,
        Error.PACOTE_INVALIDO.value,
    ]

    if response_json["status"]:
        endereco = response_json["matrizEndereco"]
        resultado = DadosEmpresa(
            razao_social=response_json["razao"],
            situacao=response_json["situacao"]["nome"],
            endereco= Endereco(
                logradouro=endereco["logradouro"],
                bairro=endereco["bairro"],
                cep=endereco["cep"],
                cidade=endereco["cidade"],
                uf=endereco["uf"],
            ),
        )
    elif response_json["erroCodigo"] == Error.BLACKLIST.value:
        resultado = Erro(
            erro=response_json["blacklist"]["motivo"],
            codigo=response_json["erroCodigo"],
        )
    elif response_json["erroCodigo"] in error_list:
        resultado = Erro(
            erro=response_json["erro"],
            codigo=response_json["erroCodigo"],
        )
    else:
        resultado = Erro(
            erro="Erro desconhecido",
            codigo=999,
        )

    return resultado.dict()