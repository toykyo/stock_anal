# Frontend (React)

## Local Development

```bash
cd frontend
npm install
npm run dev
```

Set `VITE_API_URL` in `.env` (optional) if you are not using the proxy defined in `vite.config.ts`.

## Pages

- Sector dashboard – overview of sectors and quick stats.
- Symbol detail – placeholder metric cards per symbol (ready for charts).
- Indicator overview – simple list of macro indicators.
- Keyword trends – placeholder for future keyword ingestion visuals.

React Query caches backend requests, so hooking up additional endpoints only requires adding fetchers under `src/api`.
