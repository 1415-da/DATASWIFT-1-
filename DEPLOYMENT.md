# Deployment Instructions

## Backend (Render)
1. Push the contents of the `backend/` folder to a new GitHub repository (if not already).
2. Go to https://render.com, create a new Web Service, and connect your repository.
3. Render will auto-detect Python. Set the build command to:
   ```
pip install -r requirements.txt
   ```
   and the start command to:
   ```
python app.py
   ```
4. Set the environment variable `PORT` to `10000` (or as required by your app).
5. Deploy and note your Render backend URL (e.g., `https://your-backend-service.onrender.com`).

## Frontend (Vercel)
1. Push the contents of the `frontend/` folder to a new GitHub repository (if not already).
2. Go to https://vercel.com, create a new project, and import your frontend repo.
3. In Vercel project settings, add an environment variable:
   - `NEXT_PUBLIC_BACKEND_URL` = `https://your-backend-service.onrender.com`
4. Deploy the project.

## Notes
- Update the `.env.example` in `frontend/` with your actual backend URL for local development.
- All API calls from the frontend will now use the deployed backend.
