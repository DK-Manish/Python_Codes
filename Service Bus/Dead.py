from azure.servicebus import ServiceBusClient

# Replace with your actual Service Bus connection string
CONNECTION_STR = "<connection String>"
QUEUE_NAME = "queuename"  

def delete_dead_letter_messages():
    servicebus_client = ServiceBusClient.from_connection_string(CONNECTION_STR)

    # Correctly access the dead-letter queue using 'sub_queue' argument
    with servicebus_client.get_queue_receiver(QUEUE_NAME, sub_queue="deadletter") as receiver:
        received_msgs = receiver.receive_messages(max_message_count=50)  # Adjust as needed
        for msg in received_msgs:
            receiver.complete_message(msg)  # Deletes the message
            print(f"Deleted message: {msg.message_id}")

    print("Dead-letter messages deleted successfully.")

# Run the function
delete_dead_letter_messages()