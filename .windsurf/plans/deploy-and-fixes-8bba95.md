# Plan: Django Vercel Deployment + Game Fixes

Update game3 voice prompts to speak full Uzbek sentences, redesign game2 with drag-drop and one-mistake-game-over mechanic, and prepare Django for Vercel serverless deployment.

## Tasks

### 1. Game3: Uzbek Voice Prompts
**File:** `/home/behruzbek/Desktop/Amaliyotlar/baby_game_site/templates/game3.html`
- Update `speakNumber()` function to say full sentences like "1 raqamini toping" instead of just the number
- Add proper Uzbek pronunciation hints if needed

### 2. Game2: Drag-Drop + One Mistake = Game Over
**File:** `/home/behruzbek/Desktop/Amaliyotlar/baby_game_site/templates/game2.html`
- Change current click-to-match logic to drag-and-drop (similar to game1)
- Implement one-mistake-game-over mechanic:
  - Remove attempts counter display
  - On wrong match: immediate lose modal, no retries
  - Progress bar showing matched vs total (like game3)
  - Keep confetti and win modal for correct completion

### 3. Django Vercel Deployment Setup
**Files to create/modify:**
- `/home/behruzbek/Desktop/Amaliyotlar/baby_game_site/vercel.json` - Vercel configuration
- `/home/behruzbek/Desktop/Amaliyotlar/baby_game_site/config/wsgi.py` - Ensure Vercel compatibility
- `/home/behruzbek/Desktop/Amaliyotlar/baby_game_site/requirements.txt` - Dependencies list
- `/home/behruzbek/Desktop/Amaliyotlar/baby_game_site/.vercelignore` - Exclude unnecessary files
- `/home/behruzbek/Desktop/Amaliyotlar/baby_game_site/config/settings.py` - Update for production

**Dependencies needed:**
- Django==4.2.x
- whitenoise (for static files)
- gunicorn (WSGI server)
- python-dotenv (environment variables)

### 4. Static Files Configuration
- Ensure whitenoise is configured in settings.py
- Collectstatic configuration for Vercel
- Update `STATIC_URL`, `STATIC_ROOT`, `STATICFILES_STORAGE`

### 5. Security & Environment
- Move SECRET_KEY to environment variable
- Set DEBUG=False for production
- Configure ALLOWED_HOSTS for Vercel domain

## Deployment Steps After Implementation

1. Install vercel CLI: `npm i -g vercel`
2. Login: `vercel login`
3. Run: `vercel` in project root
4. Set environment variables in Vercel dashboard
5. Deploy: `vercel --prod`
