import { useQuery } from "@tanstack/react-query";

import MetricCard from "../components/MetricCard";
import { fetchIndicators } from "../api/client";

function IndicatorOverview() {
  const { data, isLoading } = useQuery({
    queryKey: ["indicators"],
    queryFn: fetchIndicators
  });

  if (isLoading) {
    return <div>로딩중...</div>;
  }

  const indicators = data?.data ?? [];

  return (
    <div className="page">
      <header>
        <h2>경제 지표</h2>
        <p>입력된 최신 경제지표와 설계된 영향도를 확인합니다.</p>
      </header>
      <div className="grid">
        {indicators.map((indicator) => (
          <MetricCard
            key={indicator.id}
            title={indicator.name}
            subtitle={indicator.description}
            value={indicator.frequency ?? "N/A"}
          />
        ))}
      </div>
    </div>
  );
}

export default IndicatorOverview;

