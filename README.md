# 🧭 Padrão de Projeto: Observer

## 📌 Nome do Projeto
**Implementação e Estudo do Padrão de Projeto Observer**

---

## 🔍 O que é o Padrão Observer?

O **Observer** é um padrão de projeto do tipo **comportamental**. Ele define uma dependência um-para-muitos entre objetos, de forma que, quando um objeto muda de estado, todos os seus dependentes são automaticamente notificados e atualizados.

**Nomes alternativos:** Observador, Escutador, Event Listener, Assinante.

---

## 🎯 Propósito

Permitir que múltiplos objetos “observem” e reajam automaticamente às mudanças de estado de outro objeto sem criar acoplamento direto entre eles.

---

## 🧠 Problema

Imagine que um cliente esteja esperando um produto chegar em uma loja. Ele pode ir até a loja todos os dias (ineficiente), ou a loja pode enviar notificações para todos os clientes (spam).  
O Observer resolve isso permitindo que o cliente **se inscreva** para ser notificado **somente quando o produto chega**.

---

## 🛠️ Solução

Implementa-se uma classe **Sujeito (Publisher)** com métodos para **registrar**, **remover** e **notificar** **observadores (Observers)**. Os observadores reagem automaticamente a qualquer mudança de estado.


Link da apresentação: https://drive.google.com/file/d/1EE-L-0HYVerkp7xgm2ijEkgjFXAWPgmG/view?usp=drive_link
