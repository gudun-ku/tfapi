from pydoc_data.topics import topics
from fastapi import APIRouter
from confluent_kafka.admin import AdminClient, NewTopic

admin_client = AdminClient({'bootstrap.servers': 'localhost:9092'})

router = APIRouter(
    prefix="/topic",
    tags=["topic"]
)


@router.get("/")
def get_all_topics():
    topic_items = admin_client.list_topics().topics
    topics = list(topic_items.keys())
    tf_topics = list(filter(lambda x: x[:2] == "tf", topics))
    tf_topics = list(map(lambda x: x[3:], tf_topics))

    return {
        "topics": tf_topics,
        "message": None
    }


@router.post("/")
def create_topic(topic_name: str):
    new_topics = [
        NewTopic(f"tf_{topic_name}", num_partitions=3, replication_factor=1)]
    fs = admin_client.create_topics(new_topics)

    for topic, f in fs.items():
        try:
            f.result()  # {} result itself is None
        except Exception as e:
            return {
                "topic": None,
                "message": "Failed to create topic {}: {}".format(topic, e),
            }

    return {
        "topic": topic_name,
        "message": None
    }
