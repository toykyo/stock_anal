import { Navigate, Route, Routes } from "react-router-dom";

import Layout from "./components/Layout";
import IndicatorOverview from "./pages/IndicatorOverview";
import KeywordTrends from "./pages/KeywordTrends";
import SectorDashboard from "./pages/SectorDashboard";
import SymbolDetail from "./pages/SymbolDetail";

function App() {
  return (
    <Layout>
      <Routes>
        <Route path="/" element={<Navigate to="/sectors" replace />} />
        <Route path="/sectors" element={<SectorDashboard />} />
        <Route path="/symbols/:symbolId" element={<SymbolDetail />} />
        <Route path="/indicators" element={<IndicatorOverview />} />
        <Route path="/keywords" element={<KeywordTrends />} />
      </Routes>
    </Layout>
  );
}

export default App;

