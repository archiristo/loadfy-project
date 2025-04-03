# 1️⃣ Python 3.9 tabanlı bir Docker imajı kullan
FROM python:3.9

# 2️⃣ Çalışma dizinini belirle
WORKDIR /loadfy-project

# 3️⃣ Gereken paketleri yükle
RUN apt-get update && apt-get install -y ffmpeg

# 4️⃣ Projedeki dosyaları konteynere kopyala
COPY . .

# 5️⃣ Gerekli Python bağımlılıklarını yükle
RUN pip install --no-cache-dir -r requirements.txt

# 6️⃣ Flask uygulamasını başlat
CMD ["python", "app.py"]
