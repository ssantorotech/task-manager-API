import httpx

BASE_URL = "http://localhost:8000"

def main():

    with httpx.Client(base_url=BASE_URL) as client:
        response = client.post(
            "/todos", 
            json={
                "title": "New Todo", 
                "description": "A new todo item", 
                "completed": False, 
                "priorita": "alta"
                }
            )
        
        print("POST:", response.status_code)

        todo = response.json()
        todo_id = todo["id"]

        response = client.get(f"/todos/{todo_id}")
        print("GET:", response.status_code)
        print("Todo letta:", response.json())


        response = client.patch(
            f"/todos/{todo_id}",
            json={
                "title": "Updated Todo",
                "description": "An updated todo item",
                "completed": True,
                "priorita": "media"
            }
        )
        print(response.status_code)
        print("Todo aggiornata:", response.json())

        response = client.delete(f"/todos/{todo_id}")
        print("DELETE:", response.status_code)

if __name__ == "__main__":
    main()