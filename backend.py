from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer
import json

class FitJoyHandler(SimpleHTTPRequestHandler):
    # For simplicity, using a dictionary to store user data.
    users = {}

    def do_GET(self):
        # Respond to a GET request with fitness-related features.
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        # Define fitness-related features
        features = {
            "fitness_goals": "Write down some of your fitness goals in a journal. Once you complete it, check it off the box and it will feel satisfying.",
            "workout_routines": "You can access tons of workouts on Youtube for free. When you finish one you will feel proud of yourself for getting it done.",
            "nutrition_recommendations": "Incorporate lot of vegetables in your diet, fruits, and cut excess sugars. Find a diet plan that matches your dietary restrictions and fitness goals. Eating cleaner sets you up for success.",
            "social_challenges": "Connect with friends, share achievements, and participate in friendly fitness challenges.",
            "user_authentication": "Register and log in to save and track your fitness journey.",
        }

        response_data = {"features": features}
        self.wfile.write(json.dumps(response_data).encode())

    def do_POST(self):
        # Handle user registration data sent via POST request.
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        user_data = json.loads(post_data.decode())

        # For simplicity, storing user data in memory. In a real app, use a database.
        user_id = user_data.get("user_id")
        if user_id:
            self.users[user_id] = user_data

        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response_data = {"message": "Data received successfully."}
        self.wfile.write(json.dumps(response_data).encode())

if __name__ == "__main__":
    # Run the server on port 8000
    with TCPServer(("", 8000), FitJoyHandler) as httpd:
        print("Server started on port 8000.")
        httpd.serve_forever()
