document.getElementById('randomTipButton').addEventListener('click', function() {
    const tips = [
        'Remember to take breaks during long gaming sessions.',
        'Experiment with different strategies to find what works best for you.',
        'Stay updated with the latest patches and updates for your games.',
        'Join gaming forums to connect with other players and get new insights.',
        'Try out different game genres to expand your gaming experience.'
    ];
    const randomTip = tips[Math.floor(Math.random() * tips.length)];
    document.getElementById('randomTip').textContent = randomTip;
});