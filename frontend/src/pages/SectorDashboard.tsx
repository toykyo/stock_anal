import { useQuery } from "@tanstack/react-query";
import MetricCard from "../components/MetricCard";
import { fetchSectors } from "../api/client";

function SectorDashboard() {
  const { data, isLoading } = useQuery({
    queryKey: ["sectors"],
    queryFn: fetchSectors
  });

  if (isLoading) {
    return <div>로딩중...</div>;
  }

  const sectors = data?.data ?? [];

  return (
    <div className="page">
      <header>
        <h2>업종 현황</h2>
        <p>코스피/코스닥 대표 업종을 관리합니다.</p>
      </header>
      <div className="grid">
        {sectors.map((sector) => (
          <MetricCard
            key={sector.id}
            title={sector.name}
            subtitle={sector.description}
            value={sector.market ?? "N/A"}
          />
        ))}
      </div>
    </div>
  );
}

export default SectorDashboard;
