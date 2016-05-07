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