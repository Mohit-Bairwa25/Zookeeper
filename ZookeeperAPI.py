

from kazoo.client import KazooClient
from kazoo.exceptions import NoNodeError

# Create a KazooClient instance
zkClient = KazooClient(hosts='localhost:2181')

# Start the Kazoo client connection
zkClient.start()

try:
    # Ensure the base path exists
    zkClient.ensure_path("/training")

    # Check if "/training/hadoop" exists, create if it doesn't
    if not zkClient.exists("/training/hadoop"):
        zkClient.create("/training/hadoop", b"initial value")
        print("Created /training/hadoop with initial value")
    else:
        # Get the data and stat (version) of the existing node
        data, stat = zkClient.get("/training/hadoop")
        print("Existing Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

    # Update the data of the node at "/training/hadoop" to "Updated Value"
    zkClient.set("/training/hadoop", b"Updated Value")

    # Get the data and stat (version) of the node at "/training/hadoop" again (to show the update)
    data, stat = zkClient.get("/training/hadoop")

    # Print the version and data of the updated node
    print("Updated Version: %s, data: %s" % (stat.version, data.decode("utf-8")))

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the Kazoo client connection
    zkClient.stop()
