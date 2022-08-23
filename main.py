import requests


class YaUploader:
    def __init__(self, t: str):
        self.token = t

    def upload(self, file_path):
        """Метод загружает файл file_path на Яндекс.Диск"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        filename = file_path.split('/', )[-1]
        headers = {'Content-Type': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        params = {"path": f"Загрузки/{filename}", "overwrite": "true"}
        _response = requests.get(upload_url, headers=headers, params=params).json()
        href = _response.get("href", "")
        responce = requests.put(href, data=open(file_path, 'rb'))
        responce.raise_for_status()
        if responce.status_code == 201:
            return 'Успешно'
        else:
            return f"Ошибка! Код ошибки: {responce.status_code}"


if __name__ == '__main__':
    path_to_file = '/home/paintbox/Загрузки/server.jar'
    token = ''
    uploader = YaUploader(token)
    print(f"Загружаем {path_to_file.split('/', )[-1]} на Яндекс.Диск")
    result = uploader.upload(path_to_file)
    print(result)
