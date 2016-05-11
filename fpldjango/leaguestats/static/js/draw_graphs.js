function drawCTMGraph(ctm_data){
  c3.generate({
    bindto: '#cum_transfers',
    data: {
        x: 'Gameweek',
        columns: ctm_data
      }
  });
};

function drawTVGraph(tv_data){
  c3.generate({
    bindto: '#team_value',
    data: {
        x: 'Gameweek',
        columns: tv_data
      }
    });
};

function drawOPRGraph(opr_data){
  var OPRGraph = c3.generate({
    bindto: '#overall_point_rank',
    data: {
        x: 'Gameweek',
        columns: opr_data
      },
    axis: {
      y: {
        label: { // ADD
          text: 'Rank',
          position: 'outer-middle'
        },
        tick: { format: d3.format("d") },
        inverted: true,
      },
    },
    
    });
};

function drawGPWGraph(gpw_data){
  var GPWGraph = c3.generate({
    bindto: '#gamepoints_by_week',
    data: {
        x: 'Gameweek',
        columns: gpw_data,
        type: 'spline',
        types: {
            Average: 'area',
        },
      },
    axis: {
      y: {
        label: { // ADD
          text: 'Points',
          position: 'outer-middle'
        },
      },
    }
    });
};