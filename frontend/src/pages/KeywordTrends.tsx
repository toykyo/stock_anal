import MetricCard from "../components/MetricCard";

const placeholder = [
  { keyword: "금리", delta: 3.2 },
  { keyword: "코스피 전망", delta: -1.4 },
  { keyword: "환율", delta: 0.8 }
];

function KeywordTrends() {
  return (
    <div className="page">
      <header>
        <h2>경제 키워드</h2>
        <p>추후 API 연동을 대비한 플레이스홀더 화면입니다.</p>
      </header>
      <div className="grid">
        {placeholder.map((item) => (
          <MetricCard
            key={item.keyword}
            title={item.keyword}
            subtitle="검색량 증감률"
            value="준비중"
            delta={item.delta}
          />
        ))}
      </div>
    </div>
  );
}

export default KeywordTrends;

