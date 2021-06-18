# alien_invasion
---

---
2021.06.18
为了探究究竟是什么影响着pygame.event.get()，加了个延时和统计后发现，while循环中，并不是一直在等着pygame，而是不断地循环，一秒钟几千次的循环。
