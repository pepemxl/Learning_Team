import { useEffect, useState, useRef } from 'react';
import * as d3 from 'd3';

const IndexPage = () => {
  const [graphData, setGraphData] = useState(null);
  const svgRef = useRef();

  useEffect(() => {
    // Fetch data from Flask backend
    fetch('http://localhost:5000/api/data2')
      .then(response => response.json())
      .then(data => {
        setGraphData(data);
        renderGraph(data);
      })
      .catch(error => console.error('Error fetching data:', error));
  }, []);

  const renderGraph = data => {
    const svg = d3.select(svgRef.current);

    // Clear previous graph
    svg.selectAll('*').remove();

    const width = 800;
    const height = 600;

    // Agrega un borde al elemento svg
    svg.style('border', '1px solid #ccc');

    const simulation = d3.forceSimulation(data.nodes)
      .force('link', d3.forceLink(data.links).id(d => d.id).distance(100))
      .force('charge', d3.forceManyBody().strength(-200))
      .force('center', d3.forceCenter(width / 2, height / 2));

    const link = svg.selectAll('.link')
      .data(data.links)
      .enter().append('line')
      .attr('class', 'link');

    const node = svg.selectAll('.node')
      .data(data.nodes)
      .enter().append('circle')
      .attr('class', 'node')
      .attr('r', 5)
      .call(d3.drag()
        .on('start', dragstarted)
        .on('drag', dragged)
        .on('end', dragended));

    simulation.on('tick', () => {
      link.attr('x1', d => d.source.x)
        .attr('y1', d => d.source.y)
        .attr('x2', d => d.target.x)
        .attr('y2', d => d.target.y);

      node.attr('cx', d => d.x)
        .attr('cy', d => d.y);
    });

    function dragstarted(event, d) {
      if (!event.active) simulation.alphaTarget(0.3).restart();
      d.fx = d.x;
      d.fy = d.y;
    }

    function dragged(event, d) {
      d.fx = event.x;
      d.fy = event.y;
    }

    function dragended(event, d) {
      if (!event.active) simulation.alphaTarget(0);
      d.fx = null;
      d.fy = null;
    }
  };

  return (
    <div className='container'>
        <div className='main-container'>
            <div align="center">
                <h1>Interactive Network Graph</h1>
                <svg ref={svgRef} width="800" height="600"></svg>
            </div>
        </div>
    </div>
  );
};

export default IndexPage;
