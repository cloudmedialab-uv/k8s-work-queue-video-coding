import sys
import json
import pika

if len(sys.argv) < 2:
    print("The IP of Kubernetes is required")
    exit()

k8s_ip = sys.argv[1]

TIMES_FILE = "times.json"
UPLOAD_SERVER_URL = f"http://{k8s_ip}:31808/upload"
RABBITMQ_SERVER = k8s_ip
RABBITMQ_PORT = 32672
RABBITMQ_USERNAME = "user"
RABBITMQ_PASSWORD = "password"
RABBITMQ_EXCHANGE = "exhange"
RABBITMQ_ROUTING_KEY = "routing_key"
RABBITMQ_QUEUE = "queue"

credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
connection = pika.BlockingConnection(
    pika.ConnectionParameters(
        host=RABBITMQ_SERVER, port=RABBITMQ_PORT, credentials=credentials, heartbeat=20
    )
)
channel = connection.channel()
channel.queue_declare(queue=RABBITMQ_QUEUE, durable=True)


def publish(msg):
    try:
        channel.basic_publish(
            exchange=RABBITMQ_EXCHANGE,
            routing_key=RABBITMQ_ROUTING_KEY,
            body=json.dumps(msg),
        )
    except Exception:
        credentials = pika.PlainCredentials(RABBITMQ_USERNAME, RABBITMQ_PASSWORD)
        connection = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=RABBITMQ_SERVER,
                port=RABBITMQ_PORT,
                credentials=credentials,
                heartbeat=20,
            )
        )
        channel = connection.channel()
        channel.basic_publish(
            exchange=RABBITMQ_EXCHANGE,
            routing_key=RABBITMQ_ROUTING_KEY,
            body=json.dumps(msg),
        )


ffmpeg_cmd = "-i bbb_30fps_640x360_800k.mp4 -c:v libx264 out.mp4"
output_files = ["out.mp4"]
input_files = ["https://dash.akamaized.net/akamai/bbb_30fps/bbb_30fps_640x360_800k.mp4"]

msg = {
    "ffmpegParams": ffmpeg_cmd,
    "datamesh": {
        "downloadFiles": input_files,
        "uploadFiles": output_files,
        "uploadUrl": UPLOAD_SERVER_URL,
        "timesFile": TIMES_FILE,
    },
}
publish(msg)
