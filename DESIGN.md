
게임초기화
    pygame.init()
    디스플레이 초기화
    게임 객체 로딩
    Background 로딩
    Sound 로딩
    Clock 초기화

EVENT LOOP
    INFINITE LOOP
        IF event.type == pygame.QUIT
            break
        IF event.type == pygame.KEYDOWN
            키보드 제어권 전달
        
        배경초기화
        배경그리기
        객체 그리기

        디스플레이 업데이트 # pygame.display.update()
        refresh rate 보정 # clock.tick(60)

    pygame.quit()
    quit() # 종료

게임초기화()
EVENT LOOP()